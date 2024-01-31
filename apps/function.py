import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

class gaussienne():

    def plot_bilateral(aire,scale):
        fig, ax = plt.subplots(figsize=(9,6))

        # x_all and y2 definition to trace the gaussian curve
        x_all = np.arange(-50, 50, 0.001)
        y = norm.pdf(x_all,0,scale)

        # Zscore calculation for bilateral probability
        z = norm.ppf(0.5 + (aire/2),0,scale)

        # x and y delimiters under the curve thanks to -z and z (bilateral)
        x = np.arange(-z, z, 0.001)
        y2 = norm.pdf(x,0,scale)

        # Curve
        ax.plot(x_all,y)

        # absisse limitation between -4 and 4
        ax.set_xlim([-3.8*scale, 3.8*scale])

        # Filling area under the curve depending on x and y
        ax.fill_between(x,y2,alpha=0.7, color='#ffcc00')
        filled_poly = ax.fill_between(x_all, y, 0, alpha=0.2, color="#ffcc00")

        # Show % of this area
        (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')

        # Display -z and z coordinates
        plt.xlabel('Z')
        plt.ylabel('Frequency')
        plt.xticks([-z,z])
        plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])

        return fig

    def plot_unilateral(aire, scale):
        fig, ax = plt.subplots(figsize=(9,6))
        # x_all and y2 definition to trace the gaussian curve
        x_all = np.arange(-50, 50, 0.001)
        y = norm.pdf(x_all,0,scale)
        # Zscore calculation for unilateral probability
        z = norm.ppf(aire, 0, scale)

        # x and y delimiters under the curve thanks to z (unilatéral)
        x = np.arange(-10, z, 0.001)
        y2 = norm.pdf(x,0,scale)

        # Trace the curve
        ax.plot(x_all,y)

        # Limit abscisse between -4 and 4
        ax.set_xlim([-3.8*scale,4*scale])

        # Filling area under the curv depending on x and y
        ax.fill_between(x,y2,alpha=0.7, color='#ffcc00')
        filled_poly = ax.fill_between(x_all,y, alpha=0.3, color='#ffcc00')

        # Add under the curve filled area ratio
        (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')

        # Show z coordinates
        plt.xlabel('Z')
        plt.ylabel('Frequency')
        plt.xticks([z])
        plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])

        return fig

    def plot_unilateral_z(z, scale):

        fig, ax = plt.subplots(figsize=(9,6))

        # x_all and y2 definition to trace the gaussian curve thanks to pdf  function(probability density fonction)
        x = np.arange(-10, 10, 0.001)
        y = norm.pdf(x, 0, scale)

        # Define x et y delimiting area under the curve thanks to z and pdf function
        # Starting from -1O until Z
        x_fill = np.arange(-10, z, 0.001)
        # Define y thanks to pdf function
        y_fill = norm.pdf(x_fill,0, scale)

        ax.plot(x, y)
        # Limit abscisses between -4 and 4
        ax.set_xlim([-3.8*scale,3.8*scale])

        # Define Zscore probability
        aire = norm.cdf(z,0,scale)

        # Fill under curve area
        ax.fill_between(x, y, alpha=0.3, color='#ffcc00')
        # Fill the part we want
        ax.fill_between(x_fill, y_fill, alpha=0.7, color='#ffcc00')

        # Display under the curve filled ratio
        ax.text(0, .2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')

        plt.xlabel('Z')
        plt.ylabel('Frequency')
        plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])

        return fig

    def plot_bilateral_z(z,scale):
        fig, ax = plt.subplots(figsize=(9,6))

        #  x_all and y2 definition to trace the gaussian curve
        x_all = np.arange(-10, 10, 0.001)
        y2 = norm.pdf(x_all,0,scale)

        # x and y delimiters under the curve thanks to -z and z (bilateral)
        x = np.arange(-z, z, 0.001)
        y = norm.pdf(x,0,scale)
        ax.plot(x_all,y2)

        # Limit abscisses between -4 and 4
        ax.set_xlim([-3.8*scale,3.8*scale])

        # Define probability corresponding to Zscore (bilateral)
        aire = (norm.cdf(z,0,scale)-0.5)*2

        # Fill area under the curve depending on x and y
        ax.fill_between(x,y, alpha=0.7, color='#ffcc00', label=aire)

        # Display area under the curve ratio
        filled_poly = ax.fill_between(x_all,y2,0, alpha=0.3, color='#ffcc00')
        (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')

        plt.xlabel('Z')
        plt.ylabel('Frequency')
        plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])

        return fig
