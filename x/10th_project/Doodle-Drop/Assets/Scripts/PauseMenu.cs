using System.Collections;
using UnityEngine;
using System;

public class PauseMenu : MonoBehaviour
{
    public GameObject pauseMenu, pauseGame, resume;
    private SpriteRenderer spriteRenderer;
    public Sprite normal, red;
    public float waitTime;
    // Start is called before the first frame update
    void Start()
    {
        pauseMenu.SetActive(false);
        pauseGame.SetActive(true);
        spriteRenderer = resume.GetComponent<SpriteRenderer>();
    }


    public void PauseGame()
    {
        pauseMenu.SetActive(true);
        pauseGame.SetActive(false);
        Time.timeScale = 0f;
    }


    public void ChangeSprite()
    {
        spriteRenderer.sprite = red;
        Time.timeScale = (float) Math.Pow(waitTime, 5);
        StartCoroutine(ResumeGame());
    }

    IEnumerator ResumeGame()
    {
        yield return new WaitForSeconds((float) Math.Pow(waitTime, 6));
        pauseMenu.SetActive(false);
        pauseGame.SetActive(true);
        spriteRenderer.sprite = normal;
        Time.timeScale = 1f;
    }
}
