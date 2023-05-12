<template>
     <main id="main-home" class="conteiner-padrao" >
       
       <h3>Recomedação de livros</h3>

        <div id="conteiner-livros-recomendados">
                  <!-- Mudar nome das varoaveis -->
                  <div v-for="livro in livros.results" :key="livro.id">

                      <NuxtLink :to="'/auth/acervo/livro/'+livro.id">

                       <nuxt-img fit="fill" class='sobre-livros' :src="livro.capa" placeholder sizes="sm:30vw md:10vw lg:120px"/>
                     
                      </NuxtLink>
                  </div>

        </div>

        <h3>Novos livros adicionados ao acervo</h3>

        <div id="conteiner-livros-novos">
                  <!-- Mudar nome das varoaveis -->
                  <div v-for="livro in acervolivrosnovos.results" :key="livro.id">
                    <NuxtLink :to="'/auth/acervo/livro/'+livro.id">
                       <nuxt-img class='sobre-livros' :src="livro.capa" format="webp" placeholder sizes="sm:30vw md:10vw lg:120px"/>
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
    gap: 5px;
    justify-content: center;
    overflow-x: auto;
    padding: .5rem;
    background: var(--main-background-color);
    border: solid var(--colorFive);
    border-radius: 1rem;
    align-items: center;
}

h3{
    text-align: center;
    margin-bottom: 1rem;
}


@media only screen and (max-width:550px){
    #conteiner-livros-recomendados,#conteiner-livros-novos{
        justify-content: flex-start;
    }
}

</style>


<script setup>
       
   const recomedacao = ()=>{
        let response = $fetch(`http://127.0.0.1:8000/recomendacao/`,{
                    method:'GET',
                    headers:{'Content-Type':'application/json'}
            });
        
        return response
   }

   let livros = await recomedacao()


   const novoslivros = ()=>{
        let response = $fetch(`http://localhost:8000/novoslivros/`,{
                    method:'GET',
                    headers:{'Content-Type':'application/json'}
            });
        
        return response
   }

   let acervolivrosnovos = await novoslivros()
   
</script>


