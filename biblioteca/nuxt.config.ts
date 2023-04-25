// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    css:['~/assets/css/padrao.css'],
    modules: [
      '@pinia/nuxt',
      '@nuxt/image-edge',
    ],
   
    runtimeConfig: {

      public: {
        apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://127.0.0.1:8000/'
      }
    },

  })
       