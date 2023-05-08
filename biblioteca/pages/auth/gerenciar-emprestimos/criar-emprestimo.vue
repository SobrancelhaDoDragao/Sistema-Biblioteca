<template>
    <NuxtLayout>
     <TheCriarEmprestimo></TheCriarEmprestimo>
   </NuxtLayout>
 </template>

<script setup>

definePageMeta({
   middleware: 'auth'
})

</script>