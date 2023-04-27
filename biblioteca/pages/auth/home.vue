<template>
   <NuxtLayout>
     <TheSideBar></TheSideBar> <TheMain></TheMain>
  </NuxtLayout>

</template>

<script setup>

definePageMeta({
   middleware: 'auth'
})

useHead({
  title: 'Biblioteca | Home',
})

// Dados do usuário logado, as vezes não funciona redirect /auth/home server-side
const user = useUserStore()

//Na home obrigatoriamente tenho usar, pq se eu logar com o outro usuario o nome não altera
user.GetUserData()

</script>