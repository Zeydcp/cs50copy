using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class scoreKeeper : MonoBehaviour
{
    public TMP_Text scoreText;
    CapsuleSpawner capsuleSpawner;
    [SerializeField] GameObject spawner;

    void Start()
    {
        capsuleSpawner = spawner.GetComponent<CapsuleSpawner>();
    }

    void Update()
    {
        scoreText.text = capsuleSpawner.scores.ToString();
    }
}
