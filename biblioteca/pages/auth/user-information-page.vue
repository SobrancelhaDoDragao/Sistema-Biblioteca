<template>
   <NuxtLayout>
    <UserDetail></UserDetail>
  </NuxtLayout>
</template>


<script setup>

definePageMeta({
   middleware: 'auth'
})

useHead({
  title: 'Biblioteca|Perfil',
})

// Dados do usuário logado, as vezes não funciona redirect /auth/home server-side
const user = useUserStore()

// Só ira fazer o request se os dados do usuario estiver vazio
if(user.nome == ''){
    user.GetUserData()
}

</script>