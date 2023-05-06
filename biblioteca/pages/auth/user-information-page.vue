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
  title: 'Biblioteca | Perfil',
})

const user = useUserStore()

// Só ira fazer o request se os dados do usuario estiver vazio
if(user.nome == ''){
    user.GetUserData()
}

</script>