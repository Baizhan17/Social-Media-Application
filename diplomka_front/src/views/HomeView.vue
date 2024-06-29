
<template>
  <!-- <main>
    <h1>Welcome</h1>
  </main> -->
  <LandingView/>
  <FooterView/>
 
</template>
<script>
import FooterView from '@/components/FooterView.vue'
import LandingView from '@/components/LandingView.vue'
import Background from '@/components/Background.vue'
export default {
     components: {
         FooterView,
         LandingView,
         Background
   },
}
</script>