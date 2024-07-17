import { createRouter, createWebHistory } from 'vue-router';
import { useUserStore } from '@/stores/user';
import HomeView from '../views/HomeView.vue';
import SignUpView from '@/views/SignUpView.vue';
import LoginView from '@/views/LoginView.vue';
import MainView from '@/views/MainView.vue';
import SearchView from '@/views/SearchView.vue';
import ProfileView from '@/views/ProfileView.vue';
import FriendsView from '@/views/FriendsView.vue';
import PostView from '@/views/PostView.vue';
import UserChatView from '@/views/UserChatView.vue';
import AboutView from '../views/AboutView.vue';
import TrendsView from '../views/TrendsView.vue';
import EditProfileView from '@/views/EditProfileView.vue';
import EditPasswordView from '@/views/EditPasswordView.vue';
import ReportView from '../views/ReportView.vue';
const restrictedRoutesForAuthenticated = ['home', 'signup', 'login'];

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/feed',
    name: 'feed',
    component: MainView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/profile/editprofile',
    name: 'editprofile',
    component: EditProfileView
  },
  {
    path: '/profile/editprofile/password',
    name: 'editpassword',
    component: EditPasswordView
  },
  {
    path: '/profile/:id',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/profile/:id/friends',
    name: 'friends',
    component: FriendsView
  },
  {
    path: '/:id',
    name: 'postview',
    component: PostView
  },
  {
    path: '/userchat',
    name: 'userchat',
    component: UserChatView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/trends/:id',
    name: 'trendsview',
    component: TrendsView
  },
  {
    path: '/report',
    name: 'report',
    component: ReportView
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  const isAuthenticated = userStore.user.isAuthenticated;

  // Check if the route is restricted for authenticated users
  if (isAuthenticated && restrictedRoutesForAuthenticated.includes(to.name)) {
    next({ name: 'feed' }); // Redirect to the feed page
  } else {
    next(); // Proceed to the route
  }
});

export default router;
