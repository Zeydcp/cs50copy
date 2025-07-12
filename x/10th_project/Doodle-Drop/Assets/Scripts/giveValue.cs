using System.Collections;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class giveValue : MonoBehaviour
{
    [SerializeField] TMP_Text score;

    // Start is called before the first frame update
    public void Start()
    {
        string newText = staticData.valueToKeep;
        score.text = newText;
    }
}
