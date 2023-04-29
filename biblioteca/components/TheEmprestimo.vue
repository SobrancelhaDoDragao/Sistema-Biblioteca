<template>
    <main class="conteiner-padrao" >
       <h1>Empréstimos</h1>

        <nuxt-link id="criar-emprestimo-btn" class="btn-padrao" to="/auth/gerenciar-emprestimos/criar-emprestimo">
        <button id="criar-emprestimo-btn" class="btn-padrao">Novo emprestimo</button>
        </nuxt-link>
        
        <table>
            <tr><th class="colum-id">#id</th> <th class="colum-usuario" >Usuario</th> <th class="colum-livro" >Livro</th> <th class="colum-date" >Emprestimo</th> <th class="colum-date">Devolução</th> </tr>

            <tr v-for="emprestimo in emprestimos.results" :key="emprestimo.id" >
                <td class="colum-id">#{{ emprestimo.id }}</td> 
                <td class="colum-usuario">{{ emprestimo.usuario_nome }}</td> 
                <td class="colum-livro">{{ emprestimo.livro_nome }}</td>  
                <td class="colum-date" >{{ emprestimo.data_criacao }}</td> 
                <td class="colum-date">{{ emprestimo.data_devolucao }}</td>
            </tr>

        </table>
   </main>
</template>


<script setup>

const getEmprestimos = async() =>{
        
               
        const response = await $fetch('http://127.0.0.1:8000/emprestimos',{
                  method:'GET',
                  headers:{'Content-Type':'application/json'}        
        });

        return response
}

let emprestimos = await getEmprestimos()
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
    padding: 1rem;
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
</style>
