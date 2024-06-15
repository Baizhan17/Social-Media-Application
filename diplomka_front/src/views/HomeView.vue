
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
export default {
     components: {
         FooterView,
         LandingView
   },
}
</script>