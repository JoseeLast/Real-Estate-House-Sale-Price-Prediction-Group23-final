# Publish the project on GitHub and deploy the app with Streamlit Community Cloud

This guide is written for publishing through a web browser. The project files already include `app.py`, `predictor.py`, `ames_housing_model.joblib`, `ames-housing.csv`, and `requirements.txt`.

## Part A — Publish the source code using the GitHub website

1. **Download and extract the project ZIP.** Extract all files into one folder on your computer. Do not upload only the ZIP file.
2. **Sign in to GitHub.** Open https://github.com and sign in.
3. **Create a repository.** Open https://github.com/new. Use the repository name `Real-Estate-House-Sale-Price-Prediction-Group23`. Add this description: `YEEAP FUSE AI-201 Module 6: House price prediction prototype and deployment evidence.` Choose **Public** if the group is permitted to share the source/data publicly and you have checked dataset terms. Do not initialize the repository with a README, license, or `.gitignore`, because these files are included in this project. Click **Create repository**.
4. **Upload the files.** In the new repository choose **Add file → Upload files**. Drag the extracted project files and folders into the upload area, or use the file picker. Include root-level files and folders, especially `.github/workflows`, `module6`, and `project_outputs`. Make sure `app.py`, `predictor.py`, `requirements.txt`, `ames_housing_model.joblib`, and `ames-housing.csv` are at the repository root. GitHub's web uploader has per-file and upload-count limits; if it rejects a file, use the GitHub Desktop or Git workflow instead of omitting required files.
5. **Commit the upload.** Use commit message `Add Group 23 Module 6 project and deployment evidence`. Select the option to commit to `main` if it is offered, then click **Commit changes**.
6. **Verify the repository.** Open the repository home page and check that `README.md` renders. Open `app.py`, `requirements.txt`, `module6/docs`, and `module6/evidence`. Open the **Actions** tab to inspect automated test results. Do not put passwords, tokens, secret files, or private customer data in the repository.
7. **Copy the repository URL.** Use the URL shown in your browser. It should look like `https://github.com/YOUR_USERNAME/Real-Estate-House-Sale-Price-Prediction-Group23`. Replace `YOUR_USERNAME` with the real account name; do not submit the placeholder.

## Part B — Deploy the Streamlit app from GitHub

1. Confirm Part A is complete and `app.py`, `predictor.py`, `ames_housing_model.joblib`, `ames-housing.csv`, and `requirements.txt` are all in the repository root.
2. Open https://share.streamlit.io and sign in with the GitHub account that owns or can access the repository. Authorize the connection if requested.
3. Click **Create app**. Choose the option indicating you already have an app.
4. Select the GitHub repository `YOUR_USERNAME/Real-Estate-House-Sale-Price-Prediction-Group23`, branch `main`, and main file path `app.py`. If the repository does not appear, verify that the correct GitHub account is connected and that repository permissions allow access.
5. In **Advanced settings**, use a Python version supported by Streamlit Community Cloud and by the pinned dependencies. Python 3.11 is the project recommendation. The requirements file pins scikit-learn to 1.8.0 to match the saved model's recorded training environment.
6. Click **Deploy**. Review the build logs if installation or startup fails. Fix the error in the repository, commit the correction, and allow the app to redeploy.
7. **Test the live app.** Enter a neighborhood and realistic property values, click **Estimate sale price**, and verify that the USD estimate, model information, and disclaimer appear. Try a changed set of values. Confirm that the app handles an invalid year relationship or other rejected inputs clearly.
8. **Copy the deployed app URL.** Only after Streamlit finishes deploying and you have tested the page, record the actual `https://...streamlit.app` URL in the submission and README. Do not invent a URL before deployment.

## Part C — Verify the evidence for Module 6

- Open the GitHub repository in a private/incognito browser window to verify public access, if the repository is public.
- Open the Streamlit URL in a separate browser tab and verify one prediction.
- In GitHub **Actions**, record whether the tests passed. A CI test pass verifies the recorded test suite, not real-world house-price accuracy.
- Check the evaluation logs in `module6/experiment_logs` and plots/test artifacts in `module6/evidence`.
- Update the submission record with both real links: GitHub repository and Streamlit app. If the app is not successfully hosted, say so and include the ZIP and local run instructions instead.

## Part D — Record and submit the capstone presentation

Use `module6/slides/Module6_Capstone_Presentation.pptx` and `module6/docs/Capstone_Video_Script.md`. Record a presentation of no more than 10 minutes and no more than 250 MB. Show the actual live app if it has been deployed; otherwise demonstrate the local application or notebook and disclose the deployment status. Each group member should speak about their actual contribution. Do not claim that monitoring, MLflow, FastAPI, Docker, or public hosting is implemented unless it has actually been tested and is running.

## Group information

See `GROUP_CONTRIBUTIONS.md`. The contribution areas are proposed for the portfolio and should be corrected by the group if they do not reflect actual participation. Addisu Melkie Tafere is listed for GitHub repository organization and deployment documentation based on the updated Module 6 group information supplied for this submission.

## Important deadline note

The assignment details shared with the group show **11 November by 9:59** in the Canvas assignment header, while the embedded assignment text states **6 November 2026**. Check the live Canvas assignment page or confirm with the instructor which deadline controls.

## References

- GitHub Docs, “Adding a file to a repository”: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- Streamlit Docs, “Deploy your app on Community Cloud”: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- Streamlit Community Cloud: https://docs.streamlit.io/deploy/streamlit-community-cloud
