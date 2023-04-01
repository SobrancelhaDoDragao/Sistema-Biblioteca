<template>
   <NuxtLayout>
     <TheSideBar></TheSideBar> <UserDetail></UserDetail>
  </NuxtLayout>
</template>


<script setup>

definePageMeta({
   middleware: 'auth'
})

useHead({
  title: 'Biblioteca|Perfil',
})

</script>