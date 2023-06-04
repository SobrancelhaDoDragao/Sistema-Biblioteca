import { defineStore } from 'pinia'

export const useUserStore = defineStore('User', {
  state: () => {
    return {
      access:'',
      refresh:'',
      id:'',
      nome:'',
      email:'',
      foto:'',
      password:'',
      recomedacao:[],
      emprestimos:[]
    }
  },
  
  actions:{
    async GetToken(){

      this.access = useCookie('access')
      this.refresh = useCookie('refresh')

      let bearer = 'Bearer ' + this.access;

      return bearer
    },

    async GetUrlBaseRuntimeConfig(){
      // Nem sempre está disponivel no server por isso usarei try e catch
      try {
        const config = useRuntimeConfig()

        return config.public.apiBase

      } catch (error) {
        
        console.log('RuntimeConfig ainda não está disponivel')
        return "http://127.0.0.1:8000/"
      }
    
    },

    async GetUserData(){

      let bearer = await this.GetToken()
  
      let url = await this.GetUrlBaseRuntimeConfig()

      const response = await $fetch(`${url}user/`,{
          method:'GET',
          headers:{'Content-Type':'application/json',
          'Authorization': bearer,
          },
      });
      
      const user = response.results[0]
  
      this.id = user.id
      this.nome = user.nome
      this.email = user.email
      this.foto = user.foto
      this.password = user.password
    },

    async PutUserData(form){

      let bearer = await this.GetToken()
  
      // Url base do back-end
      let url = await this.GetUrlBaseRuntimeConfig()
      
      const response = await $fetch(`${url}user/${this.id}/`,{
        method:'PATCH',
        headers:{
        'Authorization': bearer,
        },
        body:form
       });
       
    },

    async GetRecomendacao(){

      // Url base do back-end
      const url = await this.GetUrlBaseRuntimeConfig()

      
      const response = await $fetch(`${url}recomendacao/`,{
                    method:'GET',
                    headers:{'Content-Type':'application/json'}
      });
        
      this.recomedacao = response
    },

    async GetLivrosEmprestimos(){

      // Url base do back-end
      const url = await this.GetUrlBaseRuntimeConfig()

      const response = await $fetch(`${url}usuarios/${this.id}/emprestimos/`,{
                    method:'GET',
                    headers:{'Content-Type':'application/json'}
       });
        
      this.emprestimos = response
    }

  }

})