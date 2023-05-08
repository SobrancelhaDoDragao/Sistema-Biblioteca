<template>
    <NuxtLayout>
     <TheVisualizarEmprestimo></TheVisualizarEmprestimo>
   </NuxtLayout>
 </template>


<script setup>

definePageMeta({
   middleware: 'auth'
})

</script>