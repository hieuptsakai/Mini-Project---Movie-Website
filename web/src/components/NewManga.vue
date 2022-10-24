<template lang="pug">
v-card
    .title
        v-icon(icon="mdi-sparkles")
        h4 New update Manga
    v-divider
    .container
        v-row 
            v-col(cols="2")
                v-dialog(v-model="dialog" max-width="80%")
                    template(v-slot:activator="{props}")
                        a(v-bind="props" ).new-manga
                            MangaIcon(name="Kowloon Generic Romance")
                    v-card 
                        MangaDetail
</template>

<script>
import { defineComponent, getCurrentInstance, ref, onMounted, computed } from 'vue'
import axios from 'axios'
import MangaIcon from "./MangaIcon.vue";
import MangaDetail from "./MangaDetail.vue";
import { mergeProps } from 'vue'

const Manga = defineComponent({
    components: {
        MangaIcon,
        MangaDetail,
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
    },
    data: () => ({
        toggle_none: null,
        toggle_one: 0,
        toggle_exclusive: 2,
        toggle_multiple: [0, 1, 2],
        dialog: false,
    }),
    methods: {
        mergeProps,
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
.new-manga:hover{
    cursor: pointer;

}
</style>
