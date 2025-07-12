using System;
using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using TMPro;

public class EndGame : MonoBehaviour
{
    [SerializeField] TMP_Text score;
    [SerializeField] GameObject Merge;
    highscore Hs;
    [SerializeField] GameObject hsText;
    public float waitTime;
    CapsuleSpawner capsuleSpawner;
    [SerializeField] GameObject spawner;
    // Game over
    public void Game_Over()
    {
        capsuleSpawner = spawner.GetComponent<CapsuleSpawner>();
        Hs = hsText.GetComponent<highscore>();
        string dataToKeep = score.text;
        staticData.valueToKeep = dataToKeep;
        if (Int16.Parse(dataToKeep) > PlayerPrefs.GetInt("HighScore", 0))
        {
            PlayerPrefs.SetInt("HighScore", Int16.Parse(dataToKeep));
            Hs.UpdateHs();
        }
        
        StartCoroutine(game_Over());
    }

    IEnumerator game_Over()
    {
        yield return new WaitForSeconds(waitTime);
        Merge.SetActive(true);
        capsuleSpawner.Kid();
        yield return new WaitForSeconds(1);
        SceneManager.LoadScene("Scenes/Game_Over");
    }
}
