<template>
      <div id="sidebar" class="conteiner-padrao">
            <h1 id="h1-side-bar">Livros emprestados</h1>

            <div id="conteiner-livros-emprestados" class="conteiner-two">
                  <!-- Mudar nome das varoaveis -->
                  <div v-for="emprestimo in teste.results" :key="emprestimo.id">

                        <NuxtLink :to="'/auth/gerenciar-emprestimos/'+emprestimo.id">
                        <nuxt-img class='sobre-livros' :src="emprestimo.LivroDados.capa" format="webp" placeholder sizes="sm:20vw md:10vw lg:120px" />
                       </NuxtLink>

                  </div>

            </div>

            <!-- Talvez colocar um Mural de aviso aqui -->

      </div>
   
</template>


<script setup>
    
   let user = useUserStore()

   await user.GetUserData()
   
  
   const emprestimos = ()=>{
        let response = $fetch(`http://127.0.0.1:8000/usuarios/${user.id}/emprestimos/`,{
                    method:'GET',
                    headers:{'Content-Type':'application/json'}
            });
        
        return response
   }
   

   let teste = await emprestimos()
   
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

#h1-side-bar{
      margin-bottom: 1rem;
}

</style>