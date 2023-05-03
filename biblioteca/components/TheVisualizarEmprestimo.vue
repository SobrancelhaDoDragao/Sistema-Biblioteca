<template>

<main class="conteiner-padrao">
    <h1>Emprestimo id: {{ id }} </h1>
</main>


</template>


<script setup>

const route = useRoute()
const id = route.params.id

</script>