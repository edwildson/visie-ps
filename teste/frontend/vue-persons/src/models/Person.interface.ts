import moment from 'moment';
export class Person {
    id: number;
    nome: string;
    rg: string;
    cpf: string;
    data_nascimento: Date;
    data_admissao: Date;
    funcao: string;
  
    constructor(
      id: number,
      nome: string,
      rg: string,
      cpf: string,
      data_nascimento: Date,
      data_admissao: Date,
      funcao: string
    ) {
      this.id = id;
      this.nome = nome;
      this.rg = rg;
      this.cpf = cpf;
      this.data_nascimento = data_nascimento;
      this.data_admissao = data_admissao;
      this.funcao = funcao;
    }
  
    formatDataAdmissao(): string {
      return `A ${moment(this.data_admissao).format('DD/MM/YYYY')}`;
    }

    formatDataNascimento(): string {
        return moment(this.data_nascimento).format('DD/MM/YYYY');
      }
  }