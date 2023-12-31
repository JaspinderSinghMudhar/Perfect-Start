# import requests
from requests import get
from bs4 import BeautifulSoup

urls = ['http://igzy.com/security-trends-in-retail/',
'http://igzy.com/sop-in-retail/',
'http://igzy.com/vms-system/',
'http://igzy.com/improve-business-efficiency/',
'http://igzy.com/retail-security-solutions/',
'http://igzy.com/camera-for-security-system/',
'http://igzy.com/unified-iot-platform/',
'http://igzy.com/iot-gateway-security-solution/',
'http://igzy.com/checkpoint-temperature-monitoring-system/',
'http://igzy.com/iot-application-security-issues/',
'http://igzy.com/warehouse-monitoring-system/',
'http://igzy.com/iot-solutions-warehouses/',
'http://igzy.com/keep-an-eye-to-your-server-room-round-the-clock/',
'http://igzy.com/security-video/',
'http://igzy.com/boost-your-business-performance-with-internet-of-things/',
'http://igzy.com/iot-retail-solution/',
'http://igzy.com/analytics-for-retail/',
'http://igzy.com/security-solutions-transformation/',
'http://igzy.com/iot-banking-solutions/',
'http://igzy.com/digital-future-with-internet-of-things/',
'http://igzy.com/usage-impact-of-iot-in-banks-and-financial-institutes/',
'http://igzy.com/secure-cloud-solutions/',
'http://igzy.com/ai-in-retail/',
'http://igzy.com/iot-platforms/',
'http://igzy.com/warehouse-management-systems/',
'http://igzy.com/surveillance-systems/',
'http://igzy.com/warehouse-safety/',
'http://igzy.com/warehouses-ready-for-ecommerce/',
'http://igzy.com/warehouse-solution/',
'http://igzy.com/iot-video-surveillance-myths/',
'http://igzy.com/video-monitoring-based-intrusion-detection-systems/',
'http://igzy.com/video-surveillance-for-enterprises/',
'http://igzy.com/cctv-camera-installation-in-warehouses/',
'http://igzy.com/security-cameras-for-your-office/',
'http://igzy.com/inventory-management/',
'http://igzy.com/smbs-in-india/',
'http://igzy.com/artificial-intelligence-of-things-aiot/',
'http://igzy.com/video-surveillance-for-office-security/',
'http://igzy.com/video-surveillance/',
'http://igzy.com/security-challenges-faced-by-gold-loan-firms-in-india/',
'http://igzy.com/smart-surveillance-solutions/',
'http://igzy.com/office-security-camera-system/',
'http://igzy.com/logistic-services/',
'http://igzy.com/healthcare-safety-security-challenges-in-india/',
'http://igzy.com/warehouse-management-measures/',
'http://igzy.com/enterprise-iot-platform/',
'http://igzy.com/atm-surveillance-with-ai-banking-solutions/',
'http://igzy.com/atm-security-with-ai-solutions/',
'http://igzy.com/surveillance-camera-the-heart/',
'http://igzy.com/security-automation/',
'http://igzy.com/cctv-surveillance/',
'http://igzy.com/enterprise-risk-management/',
'http://igzy.com/dome-camera-the-right-surveillance-device/',
'http://igzy.com/warehouse-stock-management/',
'http://igzy.com/intelligent-security-surveillance-system/',
'http://igzy.com/iot-energy-efficiency/',
'http://igzy.com/actionable-analytics/',
'http://igzy.com/the-ghost-kitchens-how-cloud-transforming-the-qsrs/',
'http://igzy.com/warehouse-automation/',
'http://igzy.com/iot-security-challenges-in-india/',
'http://igzy.com/retail-analytics/',
'http://igzy.com/wireless-security-camera-system/',
'http://igzy.com/home-automation-devices-is-your-home-really-smart/',
'http://igzy.com/cloud-video-surveillance/',
'http://igzy.com/video-security-solutions/',
'http://igzy.com/warehouse-automation-solution/',
'http://igzy.com/cloud-camera-solution-for-enterprise/',
'http://igzy.com/warehouse-safe-with-igzys-fire-safety-solution/',
'http://igzy.com/iot-approach-to-upscale-warehouse-e-surveillance/',
'http://igzy.com/server-room-security-best-practices/',
'http://igzy.com/security-solutions-for-retail/',
'http://igzy.com/cctv-cloud-storage/',
'http://igzy.com/burglar-alarm-system/',
'http://igzy.com/ip-cctv-camera/',
'http://igzy.com/bank-security-with-smart-access-control-system/',
'http://igzy.com/how-video-based-business-intelligence-helps-banks-fight-fraud/',
'http://igzy.com/smart-banking-security-solutions/',
'http://igzy.com/impact-of-iot-in-banks-and-financial-services/',
'http://igzy.com/cloud-platform-solution-in-warehouse-perimeter-intrusion-detection/',
'http://igzy.com/how-can-monitoring-employee-performance-help-you-achieve-your-long-term-goals/',
'http://igzy.com/video-surveillance-as-a-service-vsaas/',
'http://igzy.com/reasons-why-you-should-move-video-surveillance-to-the-cloud/',
'http://igzy.com/challenges-and-solutions-to-manage-bank-and-atm-security/',
'http://igzy.com/wi-fi-cctv-camera-reshaping-the-camera-market/',
'http://igzy.com/tips-to-improve-warehouse-security/',
'http://igzy.com/cloud-video-surveillance-solution-impact/',
'http://igzy.com/warehouse-security-with-cctv-installations/',
'http://igzy.com/strategies-to-follow-when-concerned-about-your-bank-security/',
'http://igzy.com/server-room-security-checklist/',
'http://igzy.com/advantages-of-iot/',
'http://igzy.com/cloud-video-recording-service/',
'http://igzy.com/warehouse-sop-security-challenges/',
'http://igzy.com/sop-in-warehouse/',
'http://igzy.com/dvr-and-nvr/',
'http://igzy.com/5-good-reasons-to-switch-to-cloud-surveillance-over-traditional-video-surveillance/',
'http://igzy.com/what-does-the-future-hold-for-cloud-surveillance/',
'http://igzy.com/keyless-locks-for-warehouses-smart-access-control-solutions/',
'http://igzy.com/warehouse-operations-with-cloud-surveillance-solutions/',
'http://igzy.com/why-is-a-cloud-security-camera-system-10x-better-than-a-traditional-cctv-system/',
'http://igzy.com/is-cloud-camera-solution-a-luxury-or-a-necessity/',
'http://igzy.com/ip-camera-installation/',
'http://igzy.com/smart-retailer/',
'http://igzy.com/iot-energy-management/',
'http://igzy.com/ai-and-ml/',
'http://igzy.com/cloud-based-service/',
'http://igzy.com/iot-services/',
'http://igzy.com/industrial-iot-applications/',
'http://igzy.com/cloud-vms/',
'http://igzy.com/cctv-camera-system/',
'http://igzy.com/security-system-for-warehouses/',
'http://igzy.com/iot-managed-services/',
'http://igzy.com/cloud-system/',
'http://igzy.com/surveillance-cameras/',
'http://igzy.com/smart-warehouse/',
'http://igzy.com/how-can-warehouse-security-cameras-sensors-improve-site-security-performance-roi-a-12-step-guide/',
'http://igzy.com/warehouse-video-surveillance/',
'http://igzy.com/what-type-of-warehouse-video-surveillance-solution-is-fit-for-your-storage-facility/',
'http://igzy.com/employee-performance-monitoring-mechanics-of-ethical-surveillance-for-sop-compliance/',
'http://igzy.com/factor-train-towards-enterprise-video-surveillance/',
'http://igzy.com/an-era-committed-to-safe-consultations-with-remote-patient-monitoring-rpm/',
'http://igzy.com/amplify-warehouse-operations-via-vsaas-solutions/',
'http://igzy.com/food-security-system/',
'http://igzy.com/local-vs-cloud-storage-video-surveillance-solution/',
'http://igzy.com/cloud-solutions-for-sme-surveillance/',
'http://igzy.com/virtual-guarding-with-igzys-smart-surveillance-solutions/',
'http://igzy.com/enabling-internet-of-things-in-retail-industry-with-igzy/',
'http://igzy.com/features-for-bank-surveillance-systems/',
'http://igzy.com/5-ways-cloud-camera-solutions-can-overcome-challenges-faced-by-traditional-cctv/',
'http://igzy.com/11-ways-iot-cloud-platforms-help-to-improve-enterprise-surveillance/',
'http://igzy.com/iot-cloud-platform/',
'http://igzy.com/cloud-video-surveillance-solution/',
'http://igzy.com/how-to-reduce-cost-and-improve-efficiency-with-a-reliable-cctv-surveillance-system/',
'http://igzy.com/cctv-cloud-storage-cameras/',
'http://igzy.com/dvr-vs-nvr-which-is-better/']


for url in urls:
  reqs = requests.get(url)
  soup = BeautifulSoup(reqs.text, 'lxml')
  for heading in soup.find_all(["h2"]):
      print(heading.name + ' ' + heading.text)  
      
      
      
      
      
      
      
