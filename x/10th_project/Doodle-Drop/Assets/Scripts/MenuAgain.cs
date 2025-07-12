using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MenuAgain : MonoBehaviour
{
    private SpriteRenderer spriteRenderer;
    public Sprite red;
    public float waitTime;

    public void ChangeColour()
    {
        spriteRenderer = GetComponent<SpriteRenderer>();
        spriteRenderer.sprite = red;
        StartCoroutine(StartAgain());
    }

    IEnumerator StartAgain()
    {
        yield return new WaitForSeconds(waitTime);
        SceneManager.LoadScene("Scenes/Menu");
    }

}
