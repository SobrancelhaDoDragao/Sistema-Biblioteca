<template>
    <main>
   
   </main>
</template>

<style scoped>
/**Colocar no lugar do sidebar um filtro de livros e formulario para cadastrar livros */

main{
   background-color: var(--main-background-color-conteiner);
   padding: 1rem;
   border-radius: 10px;
   flex: 4;
   border: solid var(--colorSix) 2px;
   
   display: grid;
   
   grid-area: "livro livros filtro filtro"
              "livro livros filtro filtro"
   ;
}

main h1{
   font-weight: var(--thin-weight);
   text-align: center;
}

.LivroConteiner{
   background: rgb(136, 129, 129);
   width: 140px;
   height: 170px;
}

#AcervoConteiner{
   display: flex;
   gap: 5px;
   margin-top: 1rem;
}

.linha{
   border-bottom: solid var(--colorSix) 2px;
   margin-top: .5rem;
}
</style>

<script setup>

      let access = useCookie('access')
      let refresh = useCookie('refresh')

      let bearer = 'Bearer ' + access;
      // Url base do back-end
      // Não fica disponivel no url /
      const config = useRuntimeConfig()
  
      const response = await $fetch(`${config.apiBase}livro/`,{
            method:'GET',
            headers:{'Content-Type':'application/json'}
      });

      const livros = response

</script>