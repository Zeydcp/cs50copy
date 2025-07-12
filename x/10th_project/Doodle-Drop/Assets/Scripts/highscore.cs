using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class highscore : MonoBehaviour
{
    [SerializeField] TMP_Text highScore;

    public void Start()
    {
        string hs = PlayerPrefs.GetInt("HighScore", 0).ToString();
        highScore.text = hs;
    }

    // Start is called before the first frame update
    public void UpdateHs()
    {
        string hs = PlayerPrefs.GetInt("HighScore", 0).ToString();
        highScore.text = hs;
    }
}
