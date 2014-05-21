package uk.co.bbc.dojo;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class FactorialCalculator1Test {

    private FactorialCalculator1 fact = new FactorialCalculator1();

    @Test
    public void shouldCalcFactorialForOne() {
        assertThat(fact.calc(1),is(1));
    }

    @Test
    public void shouldCalcFactorialForFour() {
        assertThat(fact.calc(4),is(24));
    }

    @Test
    public void shouldCalcFactorialForTen() {
        assertThat(fact.calc(10),is(3628800));
    }
}
