## Instantaneous Center Method for Diaphragms

This repository contains computational notebooks for the Instantaneous Center Method (ICM) to estimate the shear strength of steel diaphragms. It specifically considers diaphragms where different types of fasteners are employed for strength calculations. The North American Standard for the Design of Profiled Steel Diaphragm Panels, AISI S310-16, provides design rules for diaphragm shear strength, in Section D, based on the elastic analysis. The objective of this project is to ascertain whether the inelastic analysis of bare steel deck diaphragms using the ICM is a viable design method. This is done by comparing it with past test results and current elastic analysis techniques.

The AISC Steel Construction Manual, AISC 360, has incorporated inelastic analysis for both bolted and welded connections since its 8th Edition. The Instantaneous Center Method, as outlined in Brandt 1982a and 1982b, necessitates understanding the load versus deformation behavior of the fasteners. Data on these load-deformation characteristics can be found for arc-spot welds in Easterling and Snow (2008) and for screws in Moen et al. (2014), among other sources.

The ICM solutions for this project are written in Python 3. Users can execute the "test.ipynb" file on Google Colab, a web-based user interface that eliminates the need for local software downloads, to test some example diaphragms. When using Google Colab with Github to run the 'test.ipynb' file, it operates through your Google Drive. As a result, you will receive a prompt requesting permission to access your Google Drive. The developed ICM codes have been tested against diaphragm test results provided in the SDII project (https://steeli.org/?p=71) and DDM 01 (Steel Deck Institute Diaphragm Design Manual, First Edition). Detailed procedures for the ICM are available in Brandt (1982a) and Brandt (1982b).

The repository features four main code files:
1. group.py - This code provides fastener coordinates grouped by their locations, including end, edge, interior supports, and side-lap fasteners. An illustration below offers a visual representation of the fastener labels. This project ignore the resistance of the corner fasteners associated with the overhanging welds where pink X marks are present in the illustration. 
![Capture](https://github.com/hyeyoungkoh/Instantaneous-Center-Method-for-Diaphragms/assets/75875948/0473e5f0-157a-4337-8ba4-8fcdd465b88d|width=50)
2. force_function.py - This code computes the forces exerted by fasteners and their respective moments about the instantaneous center. It considers different load-deformation relationships for arc-spot welds (used for end, edge, and interior supports) and screws (utilized for side-lap fasteners). The load-deformation relationships embedded in this code are derived from the test results (Snow and Easterling 2008 and Moen et al. 2014)
3. IC.py - This code embodies an iteration process designed to estimate the final instantaneous center.
4. test.ipynb - Users can excute this file to calculate the shear strength of diaphragms. Detailed annotations are provided in the code line by line.

## References
- AISI S310, North American Specification for the Design of Profiled Steel Diaphragm Panels, AISI, 2016.
-  ANSI/AISC 360, American Institute of Steel Construction, Specification for Structural Steel Buildings, Chicago, IL, 2022.
- Brandt, G. D. Rapid Determination of Ultimate Strength of Eccentrically Loaded Bolt Groups, 1982a.
- Brandt, G. D. A General Solution for Eccentric Loads on Weld Groups, 1982b.
- Snow, G. L. and W. S. Easterling. Section properties for cellular decks subjected to negative bending. 2008.
- Moen, C. D., D. A. Padilla-Llano, S. Corner, and C. Ding. Towards load-deformation models for screw-fastened cold-formed steel-to-steel shear connections. 2014.
- SDI DDM 01, Steel Deck Institute Diaphragm Design Manual, 1981.
