<template>
    <NuxtLayout>
    <TheEmprestimo></TheEmprestimo>
   </NuxtLayout>
</template>


<script setup>

definePageMeta({
   middleware: 'auth'
})

useHead({
  title: 'Biblioteca | Emprestimos',
})

</script>