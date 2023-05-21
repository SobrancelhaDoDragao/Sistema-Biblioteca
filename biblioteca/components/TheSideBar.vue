<template>
      <div id="sidebar" class="conteiner-padrao">
            <h2 id="h2-side-bar">Livros emprestados</h2>

            <div id="conteiner-livros-emprestados" class="conteiner-two">
                  <!-- Mudar nome das varoaveis -->
                  <div v-for="emprestimo in user.emprestimos" :key="emprestimo.id">

                        <NuxtLink :to="'/auth/gerenciar-emprestimos/'+emprestimo.id">
                        <nuxt-img class='sobre-livros' :src="emprestimo.LivroDados.capa" format="png" sizes="md:20vw lg:8vw" />
                       </NuxtLink>

                  </div>

            </div>

            <!-- Talvez colocar um Mural de aviso aqui -->

      </div>
   
</template>


<script setup>
    
   let user = useUserStore()

   await user.GetUserData()

   user.GetLivrosEmprestimos()
   
</script>

<style scoped>
#sidebar{
    background-color: var(--main-background-color-conteiner);
    padding: 1rem;
    border-radius: 20px;
    flex: 2;   
}

#conteiner-livros-emprestados{
   display: flex;
   justify-content: center;
   gap: 1rem;
   /*overflow-x: auto;*/
   flex-wrap: wrap;
   padding: 1rem;
}

#h2-side-bar{
      margin-bottom: 1rem;
}

</style>