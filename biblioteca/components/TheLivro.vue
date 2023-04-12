<template>
    <main id="main-livro" class="conteiner-padrao">
       
      <nuxt-img  id="livro-detail" :src="'http://localhost:8000/static/img/'+livro.livro.capa" fit="inside" sizes='xs:50vw sm:40vw md:35vw lg:28vw xl:20vw'/>
        <div id="livro-informacao">

            <div>
            <h1>{{ livro.livro.nome }}</h1>

            <h2>Editora:{{ livro.livro.editora }}</h2>
            </div>

            <div id="acoes-livro">
                <NuxtLink to="/auth/acervo/livros" class="btn-padrao" id='btn-voltar-livro'> Voltar</NuxtLink>  <button id='btn-salvar-livro' class="btn-padrao" >Editar</button> <button id='btn-emprestimo-livro' class="btn-padrao" >Emprestar</button> <button id='btn-excluir-livro' class="btn-danger" >Excluir</button> 
            </div>
            
        </div>
    </main>
</template>

<style scoped>
#main-livro{
    flex: 4;
    display: flex;
    align-content: center;
    justify-content: center;
    gap: 1rem;
}

#livro-detail{
   border: solid 5px var(--colorFive);
}

#livro-informacao{
    width: 40%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

h1{
  font-size: 2.5rem;
  border-bottom: solid 2px var(--colorFive);
  width: 100%;
}

h2{
    margin-top: 1rem;
}

#acoes-livro{
    display: flex;
    gap: .5rem;
    border-top: solid 2px var(--colorFive);
    padding-top: 1rem;
    flex-wrap: wrap;
}

#btn-voltar-livro{
    text-decoration: none;
}
</style>

<script setup>
//
const route = useRoute()

let livro = useLivroStore()

livro.GetLivro(route.params.id)

</script>



