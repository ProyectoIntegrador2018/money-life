import { Affects } from 'src/app/shared/interfaces/affects';
export interface InitQuestion {
    Descripcion: string;
    Pregunta_id: number;
    TipoPregunta: string;
    Afecta: Affects[]
}
