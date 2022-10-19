<template lang="pug">
v-card
    .title
        v-icon(icon="mdi-sparkles")
        h4 New update Manga
    v-divider
    .container
        v-row 
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance ")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance ")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance ")
            v-col(cols="2")
                a(href="#")
                    MangaIcon(name="Kowloon Generic Romance ")
</template>

<script>
import { defineComponent, getCurrentInstance, ref, onMounted, computed } from 'vue'
import axios from 'axios'
import MangaIcon from "./MangaIcon.vue";

const Manga = defineComponent({
    components: {
        MangaIcon,
    },
    setup(){
        const mangaList = ref([])
        // const axios = require('axios').default;
        const getManga = async () => {
            await axios.get('/user?ID=12345')
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            })
            .finally(function () {
            });
        }
        onMounted(async () => {
            console.log(1123)
            getManga()
        })
    }
})

export default Manga
</script>


<style lang="scss" scoped>
.title{
    padding: 1rem;
    display: flex;
    h4{
        padding-left: 0.66rem;
    }
}
</style>
