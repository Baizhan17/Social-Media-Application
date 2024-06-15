<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        
        <RouterLink to="/profile/editprofile/password" class="text-red-300 underline">Change Password</RouterLink>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Name</label><br>
                        <input type="text" v-model="form.name" placeholder="Your full name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <!-- <div>
                        <label>Password</label><br>
                        <input type="password" v-model="form.password1" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Repeat password</label><br>
                        <input type="password" v-model="form.password2" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div> -->

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-blue-600 text-white rounded-lg">Save</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    
</template>
<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
     name: 'EditProfileView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

//     components: {
//         FeedItem
//     },

        data() {
                return {
                    form: {
                        email: this.userStore.user.email,
                        name:this.userStore.user.name,
                        photo:null
                    },
                    errors: [],
                }
            },

//     mounted() {
//         this.getFeed()
//     },

//     watch: { 
//         '$route.params.id': {
//             handler: function() {
//                 this.getFeed()
//             },
//             deep: true,
//             immediate: true
//         }
//     },

        methods: {
                submitForm() {
                    this.errors = []

                    if (this.form.email === '') {
                        this.errors.push('Your e-mail is missing')
                    }

                    if (this.form.name === '') {
                        this.errors.push('Your name is missing')
                    }

                    if (this.form.password1 === '') {
                        this.errors.push('Your password is missing')
                    }

                    if (this.form.password1 !== this.form.password2) {
                        this.errors.push('The password does not match')
                    }

                    if (this.errors.length === 0) {
                        axios
                            .post('http://127.0.0.1:8000/api/editprofile/', this.form)
                            .then(response => {
                            console.log(response.data);
                                if (response.data.message === 'new email is setted up') {
                                    this.toastStore.showToast(5000, 'Changes applied', 'bg-emerald-500')

                                    //this.form.email = ''
                                    //this.form.name = ''
                                    this.userStore.setUserInfo({
                                        id:this.userStore.user.id,
                                        name:this.form.name,
                                        email:this.form.email,
                                    })
                                    this.$router.back()
                                } else {
                                    this.toastStore.showToast(5000, `${response.data.message}. Please try again`, 'bg-red-300')
                                }
                            })
                            .catch(error => {
                                console.log(error)
                            })
                    }
                }
            }
}
</script>

