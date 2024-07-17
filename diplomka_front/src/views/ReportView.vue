<template>
<textarea class="p-4 w-full bg-gray-300 rounded-lg" placeholder="Describe the problem with the post"></textarea>

</template>

<script>
import axios from "axios"
export default {
    name: 'report',
    mathods:{
        getReportedPost(){

        },
        sendReport(){
            
        }
    }
}
</script>
<style scoped>
textarea {
    resize: none; /* Disable manual resizing */
}
</style>