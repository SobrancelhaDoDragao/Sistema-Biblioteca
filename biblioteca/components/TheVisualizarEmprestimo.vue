<template>

<main class="conteiner-padrao">
    <h1>Emprestimo</h1>

    <section id="DadosEmprestimo">

        <div class="conteiner-emprestimo">
            <h2 id="nome-usario-emprestimo" >{{ dados.UsuarioDados.nome }}</h2>
            
            <nuxt-img :src="dados.UsuarioDados.foto" quality="100" width="180" height="280" placeholder id="img-foto-usuario" />
        </div>
            

        <div class="conteiner-emprestimo">
            <h2 id="nome-livro-emprestimo">{{ dados.LivroDados.nome }}</h2>

            <nuxt-img :src="dados.LivroDados.capa" quality="100"  width="180" height="280" placeholder id="img-capa-livro"/>
        </div>
        

        <div id="datas">

            <span v-if="editar == false">Emprestimo: {{ dados.data_criacao }}</span>
            <span v-if="editar == false">Devolução: {{ dados.data_devolucao }}</span>
            
            <span v-if="editar">Devolução:</span>
            <input v-if="editar" type="datetime-local" v-model="data">
            
        </div> 

        <div id="status">
   
            <label v-if="editar" for="select-emprestimo">Status:</label>
            
            <select v-if="editar" id="select-emprestimo" v-model="selected">
                <option value="atrasado">Atrasado</option>
                <option value="devolvido">Devolvido</option>
                <option value="emprestado">Emprestado</option>
            </select>

            <span v-else >Status: {{ dados.status }}</span>
        </div>


        <div id="btn-group-emprestimo">

            <NuxtLink to="/auth/gerenciar-emprestimos/emprestimos" class="btn-padrao" id="voltar-emprestimo"><nuxt-img src="icons/arrow-left-solid.svg" width="25" height="25"/></NuxtLink> 

            <button class="btn-padrao"  id="alterar-emprestimo" v-if="editar" @click.prevent="editar = false">Cancelar</button>
            <button class="btn-padrao"  id="alterar-emprestimo" v-else @click.prevent="editar = true">Alterar emprestimo</button>

            <button class="btn-padrao" v-if="editar == true" @click="SalvarAlteracao" > Salvar</button>

            <button class="btn-padrao" @click="Excluir">Excluir</button>

        </div>
            
    </section>

</main>


</template>


<style scoped>

h1,h2{
    text-align: center;
}

h2{
    background: var(--colorFive);
    padding: 10px;
    font-weight:var(--bold-weight);
    
}

#DadosEmprestimo{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.conteiner-emprestimo{
    border: solid 2px var(--colorFive);
    border-radius: 10px;
    border: solid var(--colorFive) 5px;
    display: grid;
    grid-template-columns: 1fr 1fr;
}

#img-foto-usuario{
    /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
    grid-row: 2;
    grid-column: 1 / 3;
    display: grid;
    justify-self: center;
}

#img-capa-livro{
    grid-row: 2;
    grid-column: 1 / 3;
    display: grid;
    justify-self: center;
}

#nome-usario-emprestimo{
    grid-row: 1;
    grid-column: 1 / 3;
}

#nome-livro-emprestimo{
    grid-row: 1;
    grid-column: 1 / 3;
}

#datas{
    background: var(--colorFive);
    padding: 10px;
    gap: .5rem;
    display: flex;
}

span{
    font-size: 1.5rem;
    border-bottom: solid 3px white;
}

#status{
    background: var(--colorFive);
    padding: 10px;
    text-align: center;
}

#alterar-emprestimo{
    justify-self:flex-start;
}

#voltar-emprestimo{
    justify-self: flex-end;
}

#select-emprestimo{
  font-size: 1rem;
  font-weight: var(--bold-weight);
  align-self: center;
  padding: 5px;
  border: none;
  background: var(--main-background-color-conteiner);
  border-radius: 10px;
  width: 50%;
}
label{
    font-size: 1rem;
    font-weight: var(--bold-weight);
    margin-right: 4px;
}

#btn-group-emprestimo{
    display: flex;
    gap: 5px;
    grid-column: 1 / 3;
    flex-wrap: wrap;
    justify-content: center;
}

@media only screen and (max-width:550px){
    #DadosEmprestimo{
        grid-template-columns: 1fr;
    }
    #btn-group-emprestimo{
    grid-column: auto;
    }
}
</style>


<script setup>

let selected = ref('emprestado')
let data = ref()

const route = useRoute()
const id = route.params.id

let emprestimo = useEmprestimoStore()

let dados = await emprestimo.getEmprestimo(id)

let editar = ref(false)

let SalvarAlteracao = async ()=>{

    await emprestimo.PutEmprestimo(id,selected.value,data.value)
    dados = await emprestimo.getEmprestimo(id)
    editar.value = false
}

const Excluir = async()=>{
    await emprestimo.DeleteEmprestimo(id)
    navigateTo('/auth/gerenciar-emprestimos/emprestimos')
}
</script>