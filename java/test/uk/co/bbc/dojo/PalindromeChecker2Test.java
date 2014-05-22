package uk.co.bbc.dojo;


import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class PalindromeChecker2Test {

    private PalindromeChecker2 checker = new PalindromeChecker2();

    @Test
    public void shouldTreatBobAsPalindrome() {
        assertThat(checker.isPalindrome("bob"), is(true));
    }

    @Test
    public void shouldNotTreatBobAsPalindrome() {
        assertThat(checker.isPalindrome("bobo"), is(false));
    }

    @Test
    public void shouldIgnoreCase() {
        assertThat(checker.isPalindrome("Bob"), is(true));
    }

    @Test
    public void shouldIgnorePunctuation() {
        assertThat(checker.isPalindrome("A man, a plan, a canal: Panama"), is(true));
    }
}
