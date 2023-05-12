<template>
      <div id="sidebar">
            <h3>Livros emprestados</h3>

            <div id="conteiner-livros-emprestados">
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
    border-left:solid var(--colorFive) 10px;
    border-right:solid var(--colorFive) 10px;
}

h3{
      text-align: center;
      margin-bottom: 1rem;
}

#conteiner-livros-emprestados{
   display: flex;
   justify-content: center;
   gap: 5px;
   /*overflow-x: auto;*/
   flex-wrap: wrap;
}

</style>