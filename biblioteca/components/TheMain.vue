<template>
     <main id="main-home" class="conteiner-padrao" >
       
       <h2>Recomedação de livros</h2>

        <div id="conteiner-livros-recomendados" class="conteiner-two">
                  <!-- Mudar nome das varoaveis -->
                  <div v-for="livro in user.recomedacao" :key="livro.id">

                      <NuxtLink :to="'/auth/acervo/livro/'+livro.id">
                       
                       <nuxt-img class='sobre-livros' :src="livro.capa" format="png" sizes="sm:35vw md:20vw lg:8vw"/>
                     
                      </NuxtLink>
                  </div>

        </div>

        <h2>Novos livros adicionados ao acervo</h2>

        <div id="conteiner-livros-novos" class="conteiner-two">
                  <!-- Mudar nome das varoaveis -->
                  <div v-for="livro in livros.novoslivros" :key="livro.id">
                    <NuxtLink :to="'/auth/acervo/livro/'+livro.id">
                       <nuxt-img class='sobre-livros' :src="livro.capa" format="png" sizes="sm:35vw md:20vw lg:8vw"/>
                    </NuxtLink>
                  </div>

        </div>

    </main>
</template>

<style scoped>
#main-home{
    flex: 4;
}

#conteiner-livros-recomendados,#conteiner-livros-novos{
    display: flex;
    gap: 1rem;
    justify-content: center;
    overflow-x: auto;
    padding: 1rem;
    align-items: center;
    margin-top: .5rem;
}

#conteiner-livros-recomendados{
    margin-bottom: .5rem;
}

@media only screen and (max-width:768px){
    #conteiner-livros-recomendados,#conteiner-livros-novos{
        justify-content: flex-start;
    }
}
</style>


<script setup>
       
   let user = useUserStore()
   let livros = useLivroStore()

   // Se estiver vazio
   if(!user.recomedacao.length){
        // Recomendacao de livros
        user.GetRecomendacao()
    }
    
   livros.GetNovosLivros()
</script>


