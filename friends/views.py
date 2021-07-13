
from accounts.views import ProfileView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (
  View,
  ListView,
  CreateView,
  DetailView,
  UpdateView,
  DeleteView
)

from .models import (Friends,FriendRequest)
from accounts.models import User



# PROFILE LIST VIEW
class ProfileListView(ListView):
  queryset = Friends.objects.filter()
  context_object_name = 'profiles'
  template_name = 'friends/profile_list.html'

  def get(self,request,*args, **kwargs):
    queryset = Friends.objects.filter(received_user=request.session.get('id'))
    print("queryset",queryset)
    myFriends = list()
    for friends in queryset:
      requestedUser = User.objects.get(id=friends.requested_user)
      
      friendsDetail={'id':requestedUser.id,'name':requestedUser.name}
      myFriends.append(friendsDetail)
      print("queryset",myFriends)
    return render(request, 'friends/profile_list.html', {"title":'My Friends',"profiles":queryset})


class AllProfileListView(ListView):
  queryset = Friends.objects.filter()
  context_object_name = 'profiles'
  template_name = 'profiles/profile_list.html'

  def get(self,request,*args, **kwargs):
    friendRequests = FriendRequest.objects.filter(received_user=request.session.get('id'),active=True)
    totalRequests=list()
    for requests in friendRequests:
      userRequest = User.objects.get(id=requests.requested_user)
      friendsDetail={'id':userRequest.id,'name':userRequest.name,'requested_user':requests.requested_user}
      totalRequests.append(friendsDetail)
    allUsers = User.objects.filter(active=True)
    return render(request, 'friends/profile_list.html', {"title":'Explore Friends',"allUsers":allUsers,"friendRequests":totalRequests,"totalRequests":len(totalRequests)})

class RemoveFriend(View):
  def get(self,request,*args, **kwargs):
    Friends.objects.filter(id=request.GET.get('id')).update(active=False)
    print(request.GET.get('id'))
    return redirect(reverse('accounts:myProfile'))


class AddFriend(View):
  def get(self,request,*args, **kwargs):
    request = FriendRequest(requested_user=request.session['id'],received_user=request.GET.get('id'))
    request.save()
    return redirect(reverse('friends:profiles-list'))

class AcceptFriend(View):
  def get(self,request,*args, **kwargs):
        FriendRequest.objects.filter(requested_user=request.GET.get('id'),received_user=request.session['id']).update(active=False)
        friend_new = Friends(requested_user=request.GET.get('id'),received_user=request.session['id'])
        friend_new.save()
        return redirect(reverse('friends:profiles-list'))

class RejectFriend(View):
  def get(self,request,*args, **kwargs):
        FriendRequest.objects.filter(requested_user=request.GET.get('id'),received_user=request.session['id']).update(active=False)
      
        return redirect(reverse('friends:profiles-list'))


# # PROFILE DETAIL VIEW
class ProfileDetailView(LoginRequiredMixin, DetailView):
  queryset = Friends.objects.all()
  context_object_name = 'profile'

  def get_object(self, *args, **kwargs):
    return get_object_or_404(
      ProfileView,
      pk=self.kwargs.get('id')
    )

  def get_context_data(self, *args, **kwargs):
    context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
    context['title'] = self.get_object().name
    return context


class Search_User(ListView):
  model = User
  template_name = "friends/profile_searchuser.html"
  

  def get(self,request,*args, **kwargs):
    username = self.request.GET.get('username',' ')
    myFriends = list()

    queryset = User.objects.filter(name__icontains = username)
    for friends in queryset:
      friendsDetail={'id':friends.id,'name':friends.name}
      myFriends.append(friendsDetail)
    return render(request,self.template_name, {"title":'Search Friends',"profiles":myFriends})

