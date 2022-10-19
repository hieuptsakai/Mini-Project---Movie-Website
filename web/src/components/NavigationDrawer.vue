<template lang="pug">
v-navigation-drawer(fixed temporary height="500" permanent location="right").v-nav-draw
    v-card( class="my-auto")
        template(v-slot:prepend)
            v-list-item(two-line prepend-avatar="https://randomuser.me/api/portraits/women/81.jpg" title="User_Name" subtitle="Logged in")
        v-divider 
        v-list(height ="500px" destiny="compact" nav)
            v-card-title.text-h6 Favorite Manga
            a(href="#")
                FavManga(name="Kowloon Generic Romance")
            a(href="#")
                FavManga(name="Kowloon Generic Romance")
            a(href="#")
                FavManga(name="Kowloon Generic Romance")
            a(href="#")
                FavManga(name="Kowloon Generic Romance")
            a(href="#")
                FavManga(name="Kowloon Generic Romance")
            a(href="#")
                FavManga(name="Kowloon Generic Romance")
</template>      
  
<script>
import FavManga from './FavManga.vue';
    
    export default {
    data: () => ({}),
    components: { FavManga }
}
</script>

<style lang="scss">
.v-navigation-drawer__content{
    background-color: #fff8e1;
}
.v-card{
    margin: 0.5rem;
}
.manga-img{
    text-align: right;
    justify-content: right;
}
a{
    text-decoration: none
}
</style>