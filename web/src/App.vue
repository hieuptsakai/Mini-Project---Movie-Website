<template lang="pug">
v-app
  HeadBar
  NavBar
  v-main
    v-container(fluid)
      NewManga
  NavDrawer
    //- MangaDetail
  Footer
</template>

<script>
import HeadBar from './components/HeadBar.vue'
import NavDrawer from './components/NavigationDrawer.vue'
import LoginSite from './components/LoginSite.vue'
import Test from './components/test.vue'
import NavBar from './components/NavBar.vue'
import NewManga from './components/NewManga.vue'
import Footer from './components/Footer.vue'
import BottomNav from './components/BottomNav.vue'
import MangaDetail from './components/MangaDetail.vue'

export default {
  name: 'app',
  components:{
    HeadBar,
    LoginSite,
    Test,
    NavBar,
    NavDrawer,
    NewManga,
    Footer,
    BottomNav,
    MangaDetail
}
}
</script>

<style lang="scss" scoped>
.v-toolbar__content{
  height: 48px;
}
.v-main{
  background-color: #fff8e1;
}
.v-nav-draw{
  height: 500px;
}
</style>