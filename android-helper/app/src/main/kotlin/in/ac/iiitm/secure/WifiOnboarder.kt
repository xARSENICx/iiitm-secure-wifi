package in.ac.iiitm.secure

import android.content.Context
import android.net.wifi.WifiEnterpriseConfig
import android.net.wifi.WifiNetworkSuggestion
import android.net.wifi.WifiManager
import android.os.Build
import androidx.annotation.RequiresApi
import java.security.cert.CertificateFactory
import java.security.cert.X509Certificate

object WifiOnboarder {

    @RequiresApi(Build.VERSION_CODES.Q)
    fun onboard(context: Context): Int {
        val wifiManager = context.getSystemService(Context.WIFI_SERVICE) as WifiManager

        // 1. Load the CA Certificate from resources
        val cf = CertificateFactory.getInstance("X.509")
        val certInputStream = context.resources.openRawResource(R.raw.iiitm_ca)
        val caCert = cf.generateCertificate(certInputStream) as X509Certificate

        // 2. Configure Enterprise Settings (EAP-TTLS + PAP)
        val enterpriseConfig = WifiEnterpriseConfig().apply {
            eapMethod = WifiEnterpriseConfig.Eap.TTLS
            phase2Method = WifiEnterpriseConfig.Phase2.PAP
            caCertificate = caCert
            domainSuffixMatch = "iiitm.ac.in"
            // Credentials are left empty so the OS prompts the user on first connect
        }

        // 3. Create Suggestions for both SSIDs
        val suggestion1 = WifiNetworkSuggestion.Builder()
            .setSsid("IIITM_Secure")
            .setWpa2EnterpriseConfig(enterpriseConfig)
            .setIsAppInteractionRequired(true) // Ensures the OS shows the suggestion
            .build()

        val suggestion2 = WifiNetworkSuggestion.Builder()
            .setSsid("IIITM_Secure_5G")
            .setWpa2EnterpriseConfig(enterpriseConfig)
            .setIsAppInteractionRequired(true)
            .build()

        val suggestionsList = listOf(suggestion1, suggestion2)

        // 4. Submit to System
        return wifiManager.addNetworkSuggestions(suggestionsList)
    }
}
