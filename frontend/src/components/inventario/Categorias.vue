<template>
    <v-card
            tile
            class="px-2"
    >
        <v-row>
            <v-col cols="12" sm="12" md="6" lg="4" class="py-0 text-center">
                <v-btn class="ma-2" fab small dark color="primary" @click="agregarCategoria()">
                    <v-icon dark>mdi-plus</v-icon>
                </v-btn>
                <v-btn class="ma-2" fab small dark color="warning" @click="editarCategoria()">
                    <v-icon dark>mdi-pencil</v-icon>
                </v-btn>
                <v-btn class="ma-2" fab small dark color="error" @click="eliminarCategoria()">
                    <v-icon dark>mdi-delete</v-icon>
                </v-btn>
            </v-col>
            <v-col cols="12" sm="12" md="6" lg="8" class="py-0">
                <v-autocomplete
                        v-model="value"
                        :items="categorias"
                        :search-input="search"
                        persistent-hint
                        return-object
                        item-text="nombre"
                        hint="Categoría"
                        clearable
                ></v-autocomplete>
            </v-col>
        </v-row>
        <v-dialog
                v-model="dialog"
                max-width="350"
        >
            <v-card>
                <v-card-title>
                    <span class="title">{{ tituloFormulario }}</span>
                </v-card-title>
                <v-card-text>
                    <span
                            v-if="editedIndex === 1"
                            class="subtitle-2">
                        ¿Está seguro que desea eliminar la categoria {{editedItem.nombre}} ?
                    </span>
                    <v-text-field
                            v-if="editedIndex != 1"
                            v-model="editedItem.nombre"
                            hint="Categoría"
                            solo
                            persistent-hint
                    ></v-text-field>
                </v-card-text>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                            color="error"
                            text
                            @click="cerrar()"
                    >
                        Cancelar
                    </v-btn>

                    <v-btn
                            color="primary"
                            text
                            @click="guardar"
                    >
                        {{textoGuardar}}
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-card>
</template>
<script>
    import axios from "axios";
    export default {
        data() {
            return {
                value : null,
                categorias: [],
                dialog: false,
                search: null,
                editedIndex: -1,
                editedItem: {
                    id: '',
                    nombre: ''
                },
                defaultItem: {
                    id: '',
                    nombre: ''
                },

            }
        },

        created() {
            const ruta = 'http://localhost:8000/api/v1.0/categoria-producto/'
            axios.get(ruta).then(response => {
                this.categorias = response.data;
                var categoria = this.$store.state.producto.categoria
                if (categoria.length > 0){
                    this.value = this.categorias.filter(cat => cat.nombre === categoria)[0]
                }
            })
                .catch(error => {
                    console.log(error);
                });
        },

        computed: {
            tituloFormulario() {
                return this.editedIndex === -1 ? 'Nueva Categoría' :
                    this.editedIndex === 0 ? 'Editar Categoría' :
                        'Eliminar Categoría'
            },

            textoGuardar() {
                return this.editedIndex === 1 ? "Sí, Eliminar" : "Guardar"
            },
        },

        watch: {
            search(val) {
                val && val !== this.value && this.querySelections(val)
            },

            value() {
                if (this.value != null){
                    this.editedItem = this.value
                    this.$store.commit('setCategoriaProducto', this.value)
                }
                else{
                    this.editedItem = this.defaultItem
                    this.$store.commit('setCategoriaProducto', {nombre: ''})
                }
            }
        },

        methods: {
            agregarCategoria() {
                this.editedItem = {id: '', nombre: ''}
                this.dialog = true
            },

            editarCategoria() {
                this.editedIndex = 0
                if (this.value != null) {
                    this.dialog = true
                }
            },

            eliminarCategoria() {
                // el número 1 en editedItem indica que se a a eliminar el elemento
                if (this.value != null) {
                    this.editedIndex = 1
                    this.dialog = true
                }
            },

            cerrar() {
                this.editedIndex = -1
                this.editedItem = this.defaultItem
                this.dialog = false
            },

            guardar() {
                if (this.editedIndex === -1) {
                    const ruta = 'http://localhost:8000/api/v1.0/categoria-producto/'
                    axios.post(ruta, this.editedItem).then((response) => {
                        this.categorias.push(response.data);
                    }).catch((error) => {
                        console.log(error);
                    });
                } else if (this.editedIndex === 0) {
                    const ruta = "http://127.0.0.1:8000/api/v1.0/categoria-producto/" + this.editedItem.id + "/"
                    var item = this.editedItem // variable declarada porque en axios.put los datos del edited item se vacían
                    axios.put(ruta, this.editedItem).then(response => {
                        Object.assign(this.categorias[this.categorias.indexOf(item)], response.data)
                        this.value = null
                    })
                        .catch(error => {
                            console.log(error);
                        });
                } else {
                    const ruta = "http://localhost:8000/api/v1.0/categoria-producto/" + this.editedItem.id + "/";
                    axios.delete(ruta).then((response) => {
                        console.log(response.data);
                    }).catch((error) => {
                        console.log(error);
                    });
                    const index = this.categorias.indexOf(this.editedItem)
                    this.categorias.splice(index, 1)

                }
                this.editedItem = this.defaultItem
                this.editedIndex = -1
                this.dialog = false

            }
        }
    }
</script>