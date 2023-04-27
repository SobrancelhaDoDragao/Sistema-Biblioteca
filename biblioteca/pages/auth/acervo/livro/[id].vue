<template>
    <NuxtLayout>
     <TheLivro></TheLivro>
   </NuxtLayout>
 </template>


<script setup>

definePageMeta({
    middleware: 'auth'
  })

useHead({
    title: 'Biblioteca | Livro',
})

</script>
