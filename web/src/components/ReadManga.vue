<template lang="pug">
v-card(max-width="30%").select-chapter-afbe
    v-table
        thead
            tr
                th.text-left  <a href="#">Chapter Before</a>  
                th.text-center.mid-chapter <a href="#">Current Chap</a>
                th.text-right <a href="#">Chap After</a>
</template>

<script>

</script>

<style lang="scss">
.select-chapter-afbe{
    margin: 0 auto;
    margin-top: 2rem;
}
.mid-chapter{
    border-left: 1px solid;
    border-right: 1px solid;
}
</style>
