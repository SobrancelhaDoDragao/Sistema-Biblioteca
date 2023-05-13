<template>
    <main class="conteiner-padrao" >
       <h1>Empréstimos</h1>

        <nuxt-link id="criar-emprestimo-btn" class="btn-padrao" to="/auth/gerenciar-emprestimos/criar-emprestimo">
        <button id="criar-emprestimo-btn" class="btn-padrao">Novo emprestimo</button>
        </nuxt-link>
        
        <table>
            <tr><th class="colum-id">#id</th> <th class="colum-usuario">Usuario</th> <th class="colum-livro" >Livro</th> <th class="colum-date" >Emprestimo</th> <th class="colum-date">Devolução</th><th>Status</th></tr>
           
            <tr v-for="emprestimo in emprestimo.emprestimosDados.emprestimos" :key="emprestimo.id" @click="RedirectEmprestimo(emprestimo.id)" class="LinkEmprestimo" >

                <td>#{{ emprestimo.id }}</td> 
                <td>{{ emprestimo.UsuarioDados.nome }}</td> 
                <td>{{ emprestimo.LivroDados.nome }}</td>  
                <td>{{ emprestimo.data_criacao }}</td> 
                <td>{{ emprestimo.data_devolucao}}</td>
                <td>{{ emprestimo.status }}</td>

            </tr>

        </table>

        <div id="btn-group-pagination">

            <button class="btn-pagination" v-on:click="emprestimo.getEmprestimos(emprestimo.emprestimosDados.previousPageNumber)">Voltar</button>
            
            <button :class="{ active: emprestimo.emprestimosDados.PageActive == pagina }" class="btn-pagination" v-on:click="emprestimo.getEmprestimos(pagina)" v-for="pagina in emprestimo.emprestimosDados.quantidadePagina">{{ pagina }}</button>

            <button class="btn-pagination" v-on:click="emprestimo.getEmprestimos(emprestimo.emprestimosDados.nextPageNumber)">Proxima</button>

        </div>
   </main>
</template>


<script setup>

let emprestimo = useEmprestimoStore()

if(emprestimo.emprestimosDados.PageActive){
    emprestimo.getEmprestimos(emprestimo.emprestimosDados.PageActive)
}
else{
    emprestimo.getEmprestimos(1) //Primeira pagina
}


const RedirectEmprestimo = (id) => {
    navigateTo(`/auth/gerenciar-emprestimos/${id}`)
} 


</script>


<style scoped>
main{
    overflow: auto;
}

h1{
    text-align: center;
}

#criar-emprestimo-btn{
    margin-bottom: 1rem;
    text-decoration: none;
}

table,td,th{
    border-collapse: collapse;
    text-align: center;
    padding: .5rem;
}

table,th{
    border: 2px solid var(--colorFive);
}

td{
    border-right:2px solid var(--colorFive);
    border-bottom:2px dashed var(--colorFive);
}

table{
    width:100%;
}

th{ 
    font-weight: var(--bold-weight);
}

.LinkEmprestimo:hover{
    background: var(--main-background-color);
    cursor: pointer;
}

#btn-group-pagination{
   display: flex;
   justify-content: center;
   margin-top: .5rem;
   gap: 5px;
}

.btn-pagination{
    background: var(--main-background-color-conteiner);
    color:var(--colorTwo);
    font-weight: var(--bold-weight);
    padding:.5rem;
    border: solid 3px var(--colorFive);
    cursor: pointer;
    border-radius: 5px;
    font-size: 1rem;
}

.active{
   background: var(--colorOne);
}
</style>
