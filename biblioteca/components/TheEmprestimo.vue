<template>
    <main class="conteiner-padrao" >
       <h1>Empréstimos</h1>

        <nuxt-link id="criar-emprestimo-btn" class="btn-padrao" to="/auth/gerenciar-emprestimos/criar-emprestimo">
        <button id="criar-emprestimo-btn" class="btn-padrao">Novo emprestimo</button>
        </nuxt-link>
        
        <table>
            <tr><th class="colum-id">#id</th> <th class="colum-usuario">Usuario</th> <th class="colum-livro" >Livro</th> <th class="colum-date" >Emprestimo</th> <th class="colum-date">Devolução</th> </tr>
           
            <tr v-for="emprestimo in emprestimo.emprestimosDados.emprestimos" :key="emprestimo.id" >
                <td class="colum-id">#{{ emprestimo.id }}</td> 
                <td class="colum-usuario">{{ emprestimo.usuario_nome }}</td> 
                <td class="colum-livro">{{ emprestimo.livro_nome }}</td>  
                <td class="colum-date" >{{ emprestimo.data_criacao }}</td> 
                <td class="colum-date">{{ emprestimo.data_devolucao }}</td>
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

emprestimo.getEmprestimos(1)

if(emprestimo.emprestimosDados.PageActive){
    emprestimo.getEmprestimos(emprestimo.emprestimosDados.PageActive)
}
else{
    emprestimo.getEmprestimos(1) //Primeira pagina
}

</script>


<style scoped>

h1{
    text-align: center;
}

#criar-emprestimo-btn{
    margin-bottom: 1rem;
    text-decoration: none;
}

table,td,th{
    border: 2px solid var(--colorFive);
    width: 100%;
    border-collapse: collapse;
    text-align: center;
    padding: .5rem;
}

th{ 
    font-weight: var(--bold-weight);
}

.colum-id{
    width: 5%;
}
.colum-usuario{
    width: 40%;
}

.colum-livro{
    width: 40%;
}

.colum-date{
    width: 7%;
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
