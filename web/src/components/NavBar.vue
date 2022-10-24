<template lang="pug">
v-app-bar(color="#FCE4EC" dense hide-on-scroll="true").navbar
    v-btn(value="home").home Home
    v-btn(value="about") About
    v-menu 
        template(v-slot:activator="{props: menu}")
            v-tooltip(location="top")
                template(v-slot:activator="{props:  tooltip}")
                    v-btn(color="#000" v-bind="mergeProps(menu, tooltip)") Genre
                span Genre type
        v-list 
            v-list-item(v-for="(item, index) in items" :key="index")
                v-list-item-title {{item.title}}
    v-spacer 
    v-dialog(v-model="dialog" max-width="35%")
        template(v-slot:activator="{props}")
            v-btn(v-bind="props" value="login") Login
        v-card 
            LoginSite( name="OtaniReading")
</template>
    
<script>
import { mergeProps } from 'vue'
import LoginSite from './LoginSite.vue';


export default {
    data: () => ({
        items: [
            { title: "Genre 1" },
            { title: "Genre 2" },
            { title: "Genre 3" },
            { title: "Genre 4" },
        ],
        text: "center",
        icon: "justify",
        toggle_none: null,
        toggle_one: 0,
        toggle_exclusive: 2,
        toggle_multiple: [0, 1, 2],
        dialog: false,
    }),
    methods: {
        mergeProps,
    },
    components: { 
        LoginSite 
    }
}
</script>
    
<style lang="scss" scoped>
.v-btn{
    height: 64px;
    padding: 0rem 1.5rem;
    
}

.v-btn:hover{
    background: #ff4584;
    box-shadow: 0 0 7px #000 inset;
    color: white;
}

.home{
    background: #ff4584;
    box-shadow: 0 0 7px #000 inset;
    color: white;
}

.login{
    padding: 3rem;
}

// .v-card{
//     width: 450px;
// }

.v-overlay__content{
    align-items: center;
}
</style>