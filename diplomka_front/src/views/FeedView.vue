<template>
  <div class="flex justify-center bg-gray-100 py-6">
    <div class="max-w-7xl grid grid-cols-4 gap-4">
      <div class="main-center col-span-3 space-y-4">
        <div class="bg-white border border-gray-200 rounded-lg">
          <form method="POST" v-on:submit.prevent="submitForm">
            <div class="p-4 bg-white border border-gray-200">
              <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you thinking about?"></textarea>
            </div>
            <div class="p-4 border-t border-gray-100 flex justify-between">
              <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>
              <button class="inline-block py-4 px-6 bg-blue-600 text-white rounded-lg">Post project</button>
            </div>
          </form>
        </div>

        <!-- Rendered Posts -->
        <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in formattedPosts" :key="post.id">
          <div class="mb-6 flex items-center justify-between">
            <div class="flex items-center space-x-6">
              <img src="http://www.placecage.com/250/250">
              <p><strong>{{ post.created_by.name }}</strong></p>
            </div>
            <p class="text-gray-600">{{ post.created_at_format }}</p>
          </div>
          <p v-html="post.formattedBody"></p>
          <div class="my-6 flex justify-between">
            <div class="flex space-x-6">
              <div class="flex items-center space-x-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"></path>
                </svg>
                <span class="text-gray-500 text-xs">{{ post.likes_counter }} likes</span>
              </div>
              <div class="flex items-center space-x-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"></path>
                </svg>
                <span class="text-gray-500 text-xs">{{ post.comments_counter }} comments</span>
              </div>
            </div>
            <div>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"></path>
              </svg>
            </div>
          </div>
        </div>

        <!-- Pagination Component -->
        <nav aria-label="Page navigation example">
          <ul class="flex justify-center items-center -space-x-px h-8 text-sm">
            <li v-if="showPreviousButton">
              <a href="#" @click.prevent="loadPrevious" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                <span class="sr-only">Previous</span>
                <svg class="w-2.5 h-2.5 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4"/>
                </svg>
              </a>
            </li>
            <li v-for="page in paginationPages" :key="page">
              <a href="#" @click.prevent="loadPage(page)" :class="['flex', 'items-center', 'justify-center', 'px-3', 'h-8', 'leading-tight', page === currentPage ? 'text-white bg-green-500 hover:bg-green-600 dark:bg-green-600 dark:text-white' : 'text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white', page === currentPage ? 'rounded-none' : 'rounded-s-lg']">{{ page }}</a>
            </li>
            <li v-if="showNextButton">
              <a href="#" @click.prevent="loadNext" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                <span class="sr-only">Next</span>
                <svg class="w-2.5 h-2.5 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
                </svg>
              </a>
            </li>
          </ul>
        </nav>
      </div>
      <div class="main-right col-span-1 space-y-4 ml-4">
        <Trends />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Trends from '@/components/Trends.vue';

export default {
  name: "FeedView",
  components: {
    Trends,
  },
  data() {
    return {
      posts: [],
      body: '',
      currentPage: 1,
      showNextButton: false,
      showPreviousButton: false,
    };
  },
  computed: {
    paginationPages() {
      // Assuming you want to show pages 1, 2, 3 for the initial request
      return [1, 2, 3];
    },
    formattedPosts() {
      return this.posts.map(post => {
        return {
          ...post,
          formattedBody: post.body.split(' ').map(word => {
            if (word.length > 60) {
              return word.match(/.{1,60}/g).join('<br>');
            }
            return word;
          }).join(' ')
        };
      });
    }
  },
  mounted() {
    this.getFeed();
  },
  methods: {
    loadNext() {
      this.currentPage += 1;
      this.getFeed();
    },
    loadPrevious() {
      this.currentPage -= 1;
      this.getFeed();
    },
    loadPage(page) {
      this.currentPage = page;
      this.getFeed();
    },
    getFeed() {
      axios
        .get(`/api/posts/`, { params: { page: this.currentPage } })
        .then(response => {
          console.log('data', response.data.results);
          this.posts = response.data.results;
          this.showNextButton = Boolean(response.data.next);
          this.showPreviousButton = Boolean(response.data.previous);
        })
        .catch(error => {
          console.log('error', error);
        });
    },
    submitForm() {
      console.log('Submit form', {
        'body': this.body
      });
      axios
        .post('/api/posts/create/', { body: this.body })
        .then(response => {
          console.log('data', response.data);
          this.posts.unshift(response.data);
          this.body = '';
        })
        .catch(error => {
          console.log('error', error);
        });
    }
  }
};
</script>

<style scoped>
/* Add any scoped styles here */
</style>
