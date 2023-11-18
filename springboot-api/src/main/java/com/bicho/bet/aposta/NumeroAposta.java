package com.bicho.bet.aposta;

import lombok.Data;

import javax.persistence.Column;
import java.io.Serializable;
import java.util.List;

@Data
public class NumeroAposta implements Serializable {

    private List<Integer> numero;

    public List<Integer> getNumero() {
        return numero;
    }
}
