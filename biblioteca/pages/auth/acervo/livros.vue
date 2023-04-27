<template>
    <NuxtLayout>
     <TheAcervo></TheAcervo>
   </NuxtLayout>
 </template>

 <script setup>
  definePageMeta({
    middleware: 'auth'
  })

  useHead({
    title: 'Biblioteca | Acervo',
  })
</script>